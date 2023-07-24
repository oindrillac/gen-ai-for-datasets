# gen-ai-for-datasets
Use generative AI for generating datasets that mimic characteristics of real world datasets.

For use-cases like building customer growth forecasting models in the open without using internal customer data, we can use Generative AI techniques to generate public datasets that mimic internal company/business customer revenue data. 

Some considerations while using Generative AI when creating these datasets are listed below:
* Modeling patterns and behaviors of the original dataset such as rare events, conditional dependencies, outliers and anomalies
* Sparse data to start with, which does not provide enough context for creating a synthetic dataset
* Dealing with biased data
* Generating synthetic data and modeling the behavior of the data while preserving the confidentiality of the initial dataset.

This [blog](https://programmaticponderings.com/2023/04/18/unlocking-the-potential-of-generative-ai-for-synthetic-data-generation/) explains some of the above challenges and others.

To test the generation of synthetic data, we will use a real-world public dataset from Kaggle. The data consists of unique account IDs and monthly revenue which is used to train an open source customer growth model. More details on the project can be found [here](https://github.com/redhat-et/customer-growth-model/)
