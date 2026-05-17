from lab6_intelligent_search.bayesian.disease_network import model, inference

def query_fever_probability(has_fever: bool):
    fever_val = 1 if has_fever else 0
    result = inference.query(variables=['Disease'], evidence={'Fever': fever_val})
    return {
        "disease_probability": float(result.values[1]),
        "healthy_probability": float(result.values[0])
    }