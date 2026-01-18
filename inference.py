import tensorflow as tf

DISEASES = [
    "Pneumonia",
    "Edema",
    "Effusion",
    "Cardiomegaly",
    "Atelectasis"
]

def load_vocab(path="model/vocab.txt"):
    with open(path) as f:
        return [line.strip() for line in f]

def generate_report(model, img_f, img_l, vocab, max_len=149):
    decoder_input = tf.zeros((1, max_len), dtype=tf.int64)

    for i in range(max_len - 1):
        label_pred, text_pred = model.predict(
            [img_f, img_l, decoder_input],
            verbose=0
        )

        next_token = tf.argmax(text_pred[0, i]).numpy()
        decoder_input = tf.tensor_scatter_nd_update(
            decoder_input, [[0, i + 1]], [next_token]
        )

        if next_token == 0:
            break

    words = [vocab[t] for t in decoder_input.numpy()[0] if t > 0]
    report = " ".join(words)

    disease_probs = dict(zip(DISEASES, label_pred[0]))

    return report, disease_probs
