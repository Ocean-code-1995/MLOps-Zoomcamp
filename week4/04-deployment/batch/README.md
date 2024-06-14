## Batch deployment

* Turn the notebook for training a model into a notebook for applying the model
    - prepare notebook!

* Turn the notebook into a script:

```bash
jupyter nbconvert --to script score_gcp.ipynb
```

* Clean it and parametrize

* Provide the following data to run script
- taxi_typ
- year
- month
- run_id    

```bash
python score_gcp.py green 2021 3 614b73140c084d6392aa3bb08db42005
```


