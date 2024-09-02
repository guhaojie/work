import jieba
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import stopwordsiso as stopwords
import os


# 使用jieba进行分词
def jieba_tokenize(text):
    return ' '.join(jieba.cut(text))


def read_files_in_folder(folder_path):
    documents = []
    files = os.listdir(folder_path)
    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            with open(file_path, encoding='utf-8', errors='ignore') as f:
                content = f.readline()
                f.readline()
                line = f.readline()
                while line:
                    line = line.strip()
                    content += line
                    line = f.readline()
                documents.append(content)
    return documents


# 自定义中文停用词列表
stop_words = list(stopwords.stopwords(["zh"]))

# 对文档进行分词
tokenized_documents = [jieba_tokenize(doc)
                       for doc in read_files_in_folder('/Users/haojiegu/NEWS/')]

# 将文档转换为词频矩阵
vectorizer = CountVectorizer(stop_words=stop_words,
                             max_df=0.5,
                             min_df=10)
X = vectorizer.fit_transform(tokenized_documents)

# 使用LDA进行主题建模
num_topics = 8  # 假设分为3个主题
lda = LatentDirichletAllocation(n_components=num_topics,
                                max_iter=50,
                                learning_offset=50,
                                random_state=42,
                                verbose=1)
lda.fit(X)

# 输出每个文档的主题分布
topic_distributions = lda.transform(X)
print("文档的主题分布:")
print(topic_distributions)


# 输出每个主题的关键词
def print_top_words(model, feature_names, _n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print(f"主题 {topic_idx}:", end=" ")
        print(" ".join([feature_names[i]
                        for i in topic.argsort()[:-_n_top_words - 1:-1]]))


n_top_words = 10
tf_feature_names = vectorizer.get_feature_names_out()
print_top_words(lda, tf_feature_names, n_top_words)
