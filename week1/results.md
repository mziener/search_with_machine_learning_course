
1. Do you understand the steps involved in creating and deploying an LTR  model?  Name them and describe what each step does in your own words.

The steps for creating and deploying a LTR model can be summarized as follows (leaving out specific Opensearch steps like setting up the ltr store):
- Define a feature set (and features) relevant for the search application
- Create a mapping which transforms the data to be searched using the feature set into a format which will be compatible with the machine learning model you intend to use.
- Collect labels in an explicit or implicit way and combine them with the transformed data so that a dataset for supervised machine learning is generated.
- Setup up a train & test split and train the machine learning model.
- Integrate the model into the search application (either into the database or as a seperate service and manage the dataflow through the search application)

In the best case it should be possible to setup tight feedback loop between featureset definition, data transformation to train and test to figure out fast which features and machine learning model are best for the search application.


2. What is a feature and featureset?

A feature is a property of the entity we are looking at. For instance a fruit could a feature called color or size or whether it contains a seed or not. These 3 features together would make up a feature set. In terms of search a feature could be anything we can calculate or retrieve for a potential search result. In the setting of supervised learning we then combine the features/the featureset with the labels in order to derive a data set which we can use for the machine learning task.

3. What is the difference between precision and recall?

Technically the difference is the denominator. Both measure the amount of relevant documents from the retrieved documents. But divide that number through different values: Precision takes the retrieved documents as the denominator and gives some a sense of good returned results are. Recall takes the number of relevant documents into consideration as the denominator and thus gives an idea of how well the system "finds" documents which might have a relevancy for the search.

4. What are some of the traps associated with using click data in your model?

Click data is unbalanced and needs to be normalized in order to be useful. Otherwise some values might be very high, some strangly precise and others totally missing. Also it is difficult to assign some confidence into the data: Some queries might have a very low amount of clicks but all went to the same item. This could cause some improber modeling of the data. We need to consider the number of samples to judge the strength of the signal.  Click data is a static predictor and needs to be adapted when things in the application or the underlying data change.

5. What are some of the ways we are faking our data and how would you prevent that in your application?

The dataset is lacking impressions which are imputed based on the click data (IDEA: if it has been clicked, it must have been shown). But this is generally a rather problematic  approach since it excludes "bad searches" (not clicked->not viewed?).
In the "real world" the impressions should be tracked somehow additionally to the clicks to get a better data set.

6. What is target leakage and why is it a bad thing?

Target leakage is the introduction of information related to the label/target into the features or training process which should not be available. This causes the model to overperform and/or learn something unintended. 

7. When can using prior history cause problems in search and LTR?

Prior history specifies a context/path through the search application. This path might be sometimes different depending on the intent and situation the user is in. Furthermore, the strength of the path (number of traversals, quality of queries) needs to be taken into consideration. Additionally, we have to be very careful with the target leakage.

8. Submit your project along with your best MRR scores


Best run (on average the runs the results are rarely above the handtuned model but slightly below it.):
```
Simple MRR is 0.269
LTR Simple MRR is 0.351
Hand tuned MRR is 0.381
LTR Hand Tuned MRR is 0.407

Simple p@10 is 0.103
LTR simple p@10 is 0.143
Hand tuned p@10 is 0.157
LTR hand tuned p@10 is 0.162
Simple better: 522      LTR_Simple Better: 707  Equal: 9
HT better: 639  LTR_HT Better: 737      Equal: 20
```

Average run (slightly below):
```
Simple MRR is 0.332
LTR Simple MRR is 0.340
Hand tuned MRR is 0.431
LTR Hand Tuned MRR is 0.366

Simple p@10 is 0.092
LTR simple p@10 is 0.135
Hand tuned p@10 is 0.164
LTR hand tuned p@10 is 0.166
```
