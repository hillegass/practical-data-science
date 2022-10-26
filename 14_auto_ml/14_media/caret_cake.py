import pycaret.regression as carreg
from pycaret.datasets import get_data
from time import perf_counter
from sklearn.metrics import r2_score
from os.path import exists

version = 2
rf_base = f'randomforest_{version:03d}'
cb_base = f'catboost_{version:03d}'

t1 = perf_counter()
dataset = get_data('diamond')
train_df = dataset.sample(frac=0.9, random_state=786)
test_df = dataset.drop(train_df.index)
print(f"Data for Modeling: {train_df.shape}")
print(f"Test data:{test_df.shape}")
t2 = perf_counter()
print(f"*** Data fetch/prep: {t2 - t1:.2f} seconds")

exp1 = carreg.setup(data=train_df, target='Price')
t3 = perf_counter()
print(f"*** Setup: {t3 - t2:.2f} seconds")

best = carreg.compare_models() 
t4 = perf_counter()
print(f"*** compare_models: {t4 - t3:.2f} seconds")

print(f"*** Best = {best}")

rf_path = f"{rf_base}.pkl"
if exists(rf_path):
    final_rf = carreg.load_model(rf_base)
    print(f"*** Read from {rf_path}")
else:
    rf = carreg.create_model('rf')
    tuned_rf = carreg.tune_model(rf)
    final_rf = carreg.finalize_model(tuned_rf)
    carreg.save_model(final_rf,rf_base)
t5 = perf_counter()
print(f"*** tune_model for random forest: {t5 - t4:.2f} seconds")
print(final_rf)

cb_path = f"{cb_base}.pkl"
if exists(cb_path):
    final_cb = carreg.load_model(cb_base)
    print(f"*** Read from {cb_path}")
else:
    cb = carreg.create_model('catboost')
    tuned_cb = carreg.tune_model(cb)
    final_cb = carreg.finalize_model(tuned_cb)
    carreg.save_model(final_cb, cb_base)

t6 = perf_counter()
print(f"*** tune_model for catboost: {t6 - t5:.2f} seconds")
print(final_cb)

carreg.plot_model(final_rf, plot='feature', save=True)
carreg.plot_model(final_rf, save=True)

t7 = perf_counter()
y_pred_cb = carreg.predict_model(final_cb, data= test_df)
t8 = perf_counter()
print(f"*** Prediction with catboost: {t8 - t7:.2f} seconds")

r2_cb = r2_score(test_df.Price, y_pred_cb.prediction_label)
print(f"*** Catboost R2 on test data: {r2_cb:.4f}")

t9 = perf_counter()
y_pred_rf = carreg.predict_model(final_rf, data= test_df)
t10 = perf_counter()
print(f"*** Prediction with randomforest: {t10 - t9:.2f} seconds")

r2_rf = r2_score(test_df.Price, y_pred_rf.prediction_label)
print(f"*** Random Forest R2 on test data: {r2_rf:.4f}")



