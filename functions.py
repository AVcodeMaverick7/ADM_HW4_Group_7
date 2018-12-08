#  Functions for reading files :

def read_vocabulary(file = 'vocabulary.txt'):
    with open(file, 'r', encoding = 'utf-8') as f:
        rows = f.read().split('\n') # split the file into rows
        # dictionary structure: {word : word_id}
        vocabulary = {int(row.split('\t')[1]) : row.split('\t')[0] for row in rows[:-1]}
    return vocabulary

def read_tfid(file = 'tfid.csv'):
    tfid = {}
    #structure tfid --> {annoucement_id : [word_id1, word_id2, ....]}
    with open(file, 'r', encoding = 'utf-8') as f:
        rows = f.read().split('\n') # split the file into rows
        for row in rows:
            row_elements = row.split('\t')
            tfid[row_elements[0]] = row_elements[1:]
    return tfid

# Functions for WORDCLOUDs :

def get_words_for_annoucements(announcements_list):
    word_container = []
    for id_ann in announcements_list:
        word_id_list = tfid[str(id_ann)]
        word_container.extend([vocabulary[int(word_id)] for word_id in word_id_list[1:]])
    return word_container

def generate_wordcloud(text, name):
    wordcloud = WordCloud(max_font_size=50, background_color="white").generate(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()
    wordcloud.to_file(name +".png")
