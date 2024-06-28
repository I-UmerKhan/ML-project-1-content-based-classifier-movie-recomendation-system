# ML-Project-1-Movie-recommendation-system

I recently completed a project focused on building a movie recommendation system using content-based classification techniques. To begin, I conducted thorough preprocessing on the movie dataset, implementing tasks such as data cleaning and stemming to refine the dataset. Next, I applied vectorization using Bag of Words (BoW) to transform movie plot summaries into numerical vectors. Using these vectors, I calculated cosine similarity to measure the distances between movies based on their plot similarities. This enabled me to recommend similar movies by identifying the 5 nearest neighbors for any given movie input by the user. To ensure reusability, I serialized the dataset as a dictionary using pickle, alongside storing the computed cosine similarity scores. For deployment and presentation, I leveraged Streamlit within PyCharm to create a local host interface. This interface was designed to showcase movie recommendations interactively, displaying movie names and fetching their posters dynamically through APIs, thereby enhancing the visual appeal and usability of the recommendation system.

![image](https://github.com/I-UmerKhan/ML-Project-1-Movie-recommendation-system/assets/103349712/3767ba8b-6f2b-4c8f-bc59-1da422086d08)

![image](https://github.com/I-UmerKhan/ML-project-1-content-based-classifier-movie-recomendation-system/assets/103349712/ebec69bb-da7c-46af-9125-4617465c09a4)

