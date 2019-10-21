MESSAGE_TEXT_ATTRIBUTE = "text"

MESSAGE_RESPONSE_KEY_ATTRIBUTE = "response_key"

MESSAGE_INTENT_ATTRIBUTE = "intent"

MESSAGE_RESPONSE_ATTRIBUTE = "response"

MESSAGE_ENTITIES_ATTRIBUTE = "entities"

CLS_TOKEN = "__CLS__"


CLS_TOKEN = "__CLS__"

MESSAGE_ATTRIBUTES = [
    MESSAGE_TEXT_ATTRIBUTE,
    MESSAGE_INTENT_ATTRIBUTE,
    MESSAGE_RESPONSE_ATTRIBUTE,
]

MESSAGE_TOKENS_NAMES = {
    MESSAGE_TEXT_ATTRIBUTE: "tokens",
    MESSAGE_INTENT_ATTRIBUTE: "intent_tokens",
    MESSAGE_RESPONSE_ATTRIBUTE: "response_tokens",
}

MESSAGE_VECTOR_SPARSE_FEATURE_NAMES = {
    MESSAGE_TEXT_ATTRIBUTE: "text_sparse_features",
    MESSAGE_INTENT_ATTRIBUTE: "intent_sparse_features",
    MESSAGE_RESPONSE_ATTRIBUTE: "response_sparse_features",
}

MESSAGE_VECTOR_DENSE_FEATURE_NAMES = {
    MESSAGE_TEXT_ATTRIBUTE: "text_dense_features",
    MESSAGE_INTENT_ATTRIBUTE: "intent_dense_features",
    MESSAGE_RESPONSE_ATTRIBUTE: "response_dense_features",
}

MESSAGE_SPACY_FEATURES_NAMES = {
    MESSAGE_TEXT_ATTRIBUTE: "spacy_doc",
    MESSAGE_RESPONSE_ATTRIBUTE: "response_spacy_doc",
}

SPACY_FEATURIZABLE_ATTRIBUTES = [MESSAGE_TEXT_ATTRIBUTE, MESSAGE_RESPONSE_ATTRIBUTE]

MESSAGE_SELECTOR_PROPERTY_NAME = "response_selector"
DEFAULT_OPEN_UTTERANCE_TYPE = "default"
OPEN_UTTERANCE_PREDICTION_KEY = "response"
OPEN_UTTERANCE_RANKING_KEY = "ranking"
RESPONSE_IDENTIFIER_DELIMITER = "/"
