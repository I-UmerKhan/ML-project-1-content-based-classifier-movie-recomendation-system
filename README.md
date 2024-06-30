# ML-Project-1-Movie-recommendation-system

I recently completed a project focused on building a movie recommendation system using content-based classification techniques. To begin, I conducted thorough preprocessing on the movie dataset, which involved data cleaning and stemming to refine the dataset. After preprocessing, I applied vectorization using the Bag of Words (BoW) method to transform movie plot summaries into numerical vectors.

Using these vectors, I calculated cosine similarity to measure the distances between movies based on their plot similarities. This enabled me to recommend similar movies by identifying the five nearest neighbors for any given movie input by the user. To ensure reusability, I serialized the dataset as a dictionary using pickle, and I also stored the computed cosine similarity scores.

For deployment and presentation, I leveraged Streamlit within PyCharm to create a local host interface. This interface was designed to showcase movie recommendations interactively, displaying movie names and dynamically fetching their posters through APIs. This approach enhanced both the visual appeal and the usability of the recommendation system.

![image](https://github.com/I-UmerKhan/ML-project-1-content-based-classifier-movie-recomendation-system/assets/103349712/e963c36c-b86f-44a2-a35e-f066d25bb6b7)


![image](https://github.com/I-UmerKhan/ML-project-1-content-based-classifier-movie-recomendation-system/assets/103349712/ebec69bb-da7c-46af-9125-4617465c09a4)

