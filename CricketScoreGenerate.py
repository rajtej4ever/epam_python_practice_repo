def generate_score_and_over(ball_runscore):
    total_runs=0
    total_over=0
    for ball,runs in  ball_runscore:
        if ball%6==0:
            total_runs+=runs
            total_over += 1
            print("over: ",total_over,"runs: ",total_runs)
        else:
            total_runs += runs
            print("over x: ",total_over,"runs y: ",total_runs)



# Example data of balls and runs scored off each ball
ball_runscore = [
    (1, 1),
    (2, 4),
    (3, 0),
    (4, 6),
    (5, 1),
    (6, 2),
    (7, 0),
    (8, 4),
    (9, 1),
    (10, 6),
    (11, 0),
    (12, 1)
]

# Generating score and over based on ball and runs data
generate_score_and_over(ball_runscore)
