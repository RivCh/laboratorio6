from fastapi import FastAPI
from lab6_intelligent_search.models.route_models import RouteRequest, BayesianRequest
from lab6_intelligent_search.services.search_service import find_route
from lab6_intelligent_search.services.bayesian_service import query_fever_probability

app = FastAPI()

@app.post('/find-route')
def search_route(request: RouteRequest):
    return find_route(request.start, request.goal)

@app.post('/bayesian-inference')
def run_inference(request: BayesianRequest):
    return query_fever_probability(request.has_fever)