# Machine Learning Glucose Prediction Model
## Project Goals
Trying to play around with data from my [Dexcom G6](https://www.dexcom.com/en-CA/en-ca-dexcom-g6-cgm-system) via [xDrip](https://github.com/NightscoutFoundation/xDrip) and [Nightscout](https://nightscout.github.io/) to create a Model
that attempts to predict the values of my future glucose readings.

## Model Predictor Used
The model used was a **Gradient Boost for Multi-target regression**.

That means that the underlying model is a decision tree, with multiple outputs that are all numerical values between (hypothetically) -infinite to +infinite.

I needed to wrap the `XGBoost` model with a `MultiOutputRegressor` from `sklearn` to be able to have multiple outputs.

## Conclusion

It seems that the model was able to predict the values of up to 12 future instances
(12 * 5 minutes = 60mins) or the equivalent to 60 minutes with ~90% accuracy (I can't wrap
my head around this yet, this is crazy accurate). The model doesn't even know when I eat or inject insulin,
and it will still accurately predict my future values.

## Notes
- The model grabs N number of previous **consecutive** values.
- N is between 8 and 96
- The model needs consecutive values, it will discard any sequence that is not 5 minutes apart from each other (dexcom default reading interval).
- There's a loop in the code that creates one model per M targets. Targets means data points in the future. So if M = 5, the model is able to predict 25 minutes in the future.
- I added the time of day in minutes as a feature for the model, which improved the models' accuracy score significantly.

## Important Notes
- This is my first attempt at anything related to Machine Learning. But it's using real data, and more importantly, real data that **I** produced.
- Maybe the model can perform better

## What's Next
I'm not really sure what's next. I'm still trying to wrap my head around this.

The model is so accurate, but yet, it might not be that valuable because it does not suggest any treatments (eating or injecting insulin). In fact, the model uses my intrinsic treatments as data of it's own. What that means is that the model is trained with hidden treatments. So it might predict that a downward curve tending to dangerous levels is going to correct itself and go upwards. But that could mean that, in reality, I noticed that danger and ate something to push my levels up (hope that made sense).

If someone finds this and needs more explanations please open a pull request.