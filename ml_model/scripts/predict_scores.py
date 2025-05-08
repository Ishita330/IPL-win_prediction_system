def predict_scores(pipeline, df):
    winning_score = pipeline.predict(df)[0] + 20
    losing_score = pipeline.predict(df)[0] - 15
    return winning_score, losing_score
