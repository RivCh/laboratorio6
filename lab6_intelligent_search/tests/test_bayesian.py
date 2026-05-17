from lab6_intelligent_search.services.bayesian_service import query_fever_probability

def test_bayesian_inference():
    result = query_fever_probability(has_fever=True)
    assert "disease_probability" in result
    assert 0.0 <= result["disease_probability"] <= 1.0