ML Risk Classifier Module

This module contains a supervised machine learning classifier
that predicts cross-examination / clarification risk for
witness statements.

Input:
- Cleaned witness statement text

Output:
- Risk probability score
- Binary risk classification (threshold-tuned)

The classifier is trained using annotated legal statements
and evaluated using standard ML metrics including accuracy,
confusion matrix, and ROC curve.
