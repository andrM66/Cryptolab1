from operator import indexOf


def cypher_text(input_filename: str, output_filename: str, key_filename) -> None:
    f = open(input_filename)
    open_text = f.read()
    f.close()
    f = open(key_filename)
    key = f.read()
    f.close()
    key = list(key.split(" "))
    key = list(map(int, key))
    key_length = len(key)
    result = []
    tmp_text_array = ""
    tmp_text_array = tmp_text_array.zfill(18)
    tmp_text_array = tmp_text_array.replace("0", " ")
    tmp_text_array = list(tmp_text_array)
    for i in range(len(open_text)):
        tmp_text_array[key[i%key_length]] = open_text[i]
        if i % key_length == 17:
            result = result + tmp_text_array
            tmp_text_array = " "
            tmp_text_array = tmp_text_array.zfill(18)
            tmp_text_array = tmp_text_array.replace("0", " ")
            tmp_text_array = list(tmp_text_array)
    result = result + tmp_text_array
    f = open(output_filename, "w")
    result = "".join(result)
    f.write(result)
    f.close()


def decypher_text(input_filename: str, key_filename: str, output_filename: str) -> None:
    f = open(input_filename)
    cyphered_text = f.read()
    f.close()
    f = open(key_filename)
    key = f.read()
    f.close()
    key = list(key.split(" "))
    key = list(map(int, key))
    key_length = len(key)
    result = []
    tmp_text_array = ""
    tmp_text_array = tmp_text_array.zfill(18)
    tmp_text_array = tmp_text_array.replace("0", " ")
    tmp_text_array = list(tmp_text_array)
    tmp_cyphered_text = [list(cyphered_text[i:i + key_length]) for i in range(0, len(cyphered_text), key_length)]
    print(tmp_cyphered_text)
    for i in range(len(cyphered_text)):
        tmp_text_array[i % key_length] = tmp_cyphered_text[i // key_length][ indexOf(key, i % key_length)]
        if i % key_length == 17:
            result = result + tmp_text_array
            tmp_text_array = " "
            tmp_text_array = tmp_text_array.zfill(18)
            tmp_text_array = tmp_text_array.replace("0", " ")
            tmp_text_array = list(tmp_text_array)
    result = result + tmp_text_array
    f = open(output_filename, "w")
    result = "".join(result)
    f.write(result)
    f.close()
    print(result)



if __name__ == '__main__':
    cypher_text("open_text.txt", "test.txt", "cyph_key.txt")
    decypher_text("test.txt", "cyph_key.txt", "result.txt")