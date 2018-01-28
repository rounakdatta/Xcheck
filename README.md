# Problem Statement

Often sensational news is created and spread through social media to achieve intended end. On the other hand, it may also involve narration of a true fact however being deliberately exaggerated. This may also affect the affect the importance of serious news media. The problem is to identify the authenticity of the news and online content. Equally important problem is to identify the bots involved in spreading false news.

## Approach
* The problem can be broken down into 3 statements :-
..1. Use NLP to check the authenticity of a news article.
..2. If the user has a query about the authenticity of a search query then we he/she can directly search on our platform and using our custom algorithm we output a confidence score.
..3. Check the authenticity of a news source.

* Articles can be analyzed by feeding them to a machine learning model (Passive Aggressive Classifier) which predicts the genuinity of the content after it's trained through predefined datasets of classified real and fake news.
* Keywords can be analyzed by doing a cross-verification on Google and ensuring if the news corresponding to the keywords have been covered by reliable and known=for=good news sources and aggregators.
* A certain URL can be analyzed if it's a real, true news provider by trying it with the classified datasets of real and fake websites.

## Application

When the fake-news detector is hosted locally / on a cloud platform, it can predict fake news with reasonable accuracy. Since edge cases of fake-news detection are controversial, the tool outputs a probability percentage instead of a rigid label.


