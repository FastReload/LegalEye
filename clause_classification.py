import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

class ClauseClassifier:
    def __init__(self, model_name='nlpaueb/legal-bert-base-uncased', device='cuda' if torch.cuda.is_available() else 'cpu'):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name).to(device)
        self.device = device
        self.label_map = {
            0: "Termination",
            1: "Liability",
            2: "Governing Law",
            3: "Confidentiality",
            4: "Dispute Resolution"
        }

    def classify(self, clauses):
        inputs = self.tokenizer(clauses, return_tensors="pt", padding=True, truncation=True).to(self.device)
        with torch.no_grad():
            logits = self.model(**inputs).logits
        label_indices = torch.argmax(logits, dim=1).cpu().tolist()
        labels = [self.label_map[idx] for idx in label_indices]
        return labels
