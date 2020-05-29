from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

stopwords = set(STOPWORDS)
comment_words = "travel accomodation pandemic tiredness malpractice biasing cheating evaluation exams paper trees doubt error unequipped terrible"


wordcloud = WordCloud(background_color ='black',
                stopwords = stopwords,
                min_font_size = 10).generate(comment_words)


plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()