import streamlit as st
import io
from clause_extraction import extract_clauses_from_pdf
from clause_classification import ClauseClassifier
from clause_matching import ClauseMatcher
from explanation_generator import ExplanationGenerator
import prepare_ledgar_index
import os

st.set_page_config(page_title="Legal Document Analyzer", layout="wide")

st.title("📄 Legal Document Analyzer")
st.write("Upload a contract PDF, press 'Run Analysis', and see extracted clauses, classifications, matches, and explanations.")

# Initialize session state
if "classifier" not in st.session_state:
    st.session_state.classifier = ClauseClassifier()
if "matcher" not in st.session_state:
    st.session_state.matcher = ClauseMatcher('ledgar_index.faiss', 'ledgar_embeddings.npy')
if "explanator" not in st.session_state:
    st.session_state.explanator = ExplanationGenerator()
if "file_ready" not in st.session_state:
    st.session_state.file_ready = False
if "file_buffer" not in st.session_state:
    st.session_state.file_buffer = None

uploaded_file = st.file_uploader("Upload Contract PDF", type=["pdf"])

if uploaded_file:
    # Store the uploaded file as a BytesIO buffer in session state
    st.session_state.file_buffer = io.BytesIO(uploaded_file.read())
    st.session_state.file_ready = True
    st.success("File uploaded and ready for analysis.")

if st.session_state.get("file_ready") and st.button("Run Analysis"):
    with st.spinner("Preparing models and data..."):
        if not (os.path.exists("ledgar_index.faiss") and os.path.exists("ledgar_embeddings.npy")):
            st.warning("FAISS index not found. Building LEDGAR index... This may take a few minutes.")
            prepare_ledgar_index.build_ledgar_index()
        st.success("All models and data ready.")

        # Process the in-memory PDF
        clauses = extract_clauses_from_pdf(st.session_state.file_buffer)
        st.write(f"Extracted {len(clauses)} clauses.")
        if not clauses:
            st.warning("No clauses were extracted. Please check the PDF content.")
        else:
            for idx, clause in enumerate(clauses):
                st.markdown(f"### Clause {idx+1}")
                st.markdown(f"**Clause Text:** {clause}")

                label = st.session_state.classifier.classify([clause])[0]
                st.markdown(f"**Legal Category:** {label}")

                matches = st.session_state.matcher.match(clause)
                st.markdown("**Top 5 LEDGAR Matches:**")
                context = []
                for match in matches:
                    st.markdown(f"- Similar Clause ID: {match['id']} (Distance: {match['distance']:.4f})")
                    context.append(f"Similar clause {match['id']}:\n{match['text']}")

                context_str = "\n\n".join(context)
                explanation = st.session_state.explanator.generate(clause, context_str)
                st.markdown(f"**Explanation:** {explanation}")

                st.markdown("---")

        # Reset session state for next file
        st.session_state.file_ready = False
        st.session_state.file_buffer = None

    st.success("Analysis complete!")
