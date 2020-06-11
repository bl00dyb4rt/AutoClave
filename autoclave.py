# -*- coding: utf-8 -*-
"""
Created on 2020-06-11
@author: b4rt
@mail: root.jmn@gmail.com
"""
import argparse
import subprocess
from pprint import pprint

from decrypt import Decrypt


class Autoclave:

    def arguments(self):
        cipher_parse = argparse.ArgumentParser(description='Encrypt and Decrypt words', add_help=True)
        cipher_parse.add_argument('-w', '--word', dest='word', action='store',
                                  help='word to encrypt', required=True)
        cipher_parse.add_argument('-k', '--key', dest='key', action='store',
                                  help='key', default='marketing')
        group = cipher_parse.add_mutually_exclusive_group(required=True)
        group.add_argument('-e', '--encrypt', dest='type', action='store_true', help='-e to encrypt')
        group.add_argument('-d', '--decrypt', dest='type', action='store_false', help='-d to decrypt')

        args = cipher_parse.parse_args()
        word = str(args.word).lower()
        key = str(args.key).lower()
        # true, Encrypt
        # False, Decrypt

        enter_type = args.type

        if enter_type:
            text_intro = "         +-+-+-+-+-+ +-+-+-+-+-++-+-+-+-+-++-+-+-+-+-+ \n" \
                         + "         |E|n|c|r|y|p|t| |W|o|r|d| |by| |B|4|r|t|\n" \
                         + "        +-+-+-+-+-+ +-+-+-+-+-++-+-+-+-+-++-+-+-+-+-+\n"
            subprocess.run(['echo', text_intro])
            subprocess.run(['echo', 'Processing... \n'])

            dict_splited_word = self.split_and_count(word)
            final_key = self.generate_key_from_password(dict_splited_word['without_spaces'], key)

            final_key_1 = self.rearming_text({
                'without_spaces': final_key,
                'list_from_spaces': dict_splited_word['list_from_spaces']
            })
            encrypted_text = self.generate_encrypted_word(dict_splited_word['without_spaces'], final_key)

            encrypted_text_1 = self.rearming_text({
                'without_spaces': encrypted_text,
                'list_from_spaces': dict_splited_word['list_from_spaces']
            })

            subprocess.run(['echo', "\n Original Text : " + word.upper()])
            subprocess.run(['echo', "\n Original Key : " + key.upper()])
            subprocess.run(['echo', "\n Original Generated Key : " + final_key_1.upper()])
            subprocess.run(['echo', "\n Encrypted Word : " + encrypted_text_1.upper()])

        else:
            text_intro = "         +-+-+-+-+-+ +-+-+-+-+-++-+-+-+-+-++-+-+-+-+-+ \n" \
                         + "         |D|e|c|r|y|p|t| |W|o|r|d| |by| |B|4|r|t|\n" \
                         + "        +-+-+-+-+-+ +-+-+-+-+-++-+-+-+-+-++-+-+-+-+-+\n"
            subprocess.run(['echo', text_intro])
            subprocess.run(['echo', 'Processing... \n'])
            subprocess.run(['echo', 'Decrypt....! \n'])
            decrypt = Decrypt()
            decrypted_word = decrypt.recursive_decrypt(message=word, key_pwd=key)['decrypted_word']
            decrypted_list = decrypt.recursive_decrypt(message=word, key_pwd=key)['decrypted_list']
            key_pwd_list = decrypt.recursive_decrypt(message=word, key_pwd=key)['key_pwd_list']

            subprocess.run(['echo', "\n Encrypted Text : " + word.upper()])
            subprocess.run(['echo', "\n Key : " + key.upper()])
            subprocess.run(['echo', "\n Decrypted Text : " + decrypted_word.upper()])

            # pprint(decrypted_list)
            # pprint(key_pwd_list)


    def vigeniere_list(self):
        """
        generate the Vigeniere Array
        :return:
        """
        alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                         'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        length_alp = len(alphabet_list)
        final_list = []
        for i in range(length_alp):
            tmp_list = []
            if i > length_alp - 1:
                i = i - length_alp
            for j in range(length_alp):
                i = i + 1
                if i > length_alp - 1:
                    i = i - length_alp
                tmp_list.append(alphabet_list[i])

            final_list.append(tmp_list)
        del final_list[-1]
        final_list.insert(0, alphabet_list)

        # print(*final_list,sep="\n")
        return final_list

    def generate_encrypted_word(self, message, key):
        """
        return the encrypted word
        :param message:
        :param key:
        :return:
        """
        vigeniere_list = self.vigeniere_list()
        final_list = []
        final_word = ''
        for i in range(len(message)):
            final_list.append([int(vigeniere_list[0].index(message[i])), int(vigeniere_list[0].index(key[i]))])
        for f in final_list:
            final_word += vigeniere_list[f[0]][f[1]]
        return final_word

    def generate_key_from_password(self, message, password):
        """
        return the key with the same message length
        :param message:
        :param password:
        :return:
        """
        length_key = len(message) - len(password)
        final_message = ''
        for i in range(length_key):
            final_message += message[i]
        return password + final_message

    def split_and_count(self, word):
        word_split = word.split()
        final_word = word.replace(" ", "")
        final_list = []
        for w in word_split:
            final_list.append(len(w))

        return {'word_without_spaces': final_word,
                'list_from_spaces': final_list}

    def split_and_count(self, text):
        word_split = text.split()
        final_word = text.replace(" ", "")
        final_list = []
        count = 0
        for w in word_split:
            count += len(w)
            final_list.append(count)

        return {'without_spaces': final_word,
                'list_from_spaces': final_list}

    def rearming_text(self, dict_word):
        final_word = ''
        count_status = 0
        for l in dict_word['list_from_spaces']:
            final_word += dict_word['without_spaces'][count_status:l] + ' '
            count_status = l

        return final_word

    def decrypt_text(self, message, key):
        message_crypted = message[0:len(key)]
        final_list = []
        for m in message_crypted:
            final_list.append([self.numberxposition(), key[message.index(m)]])

    def numberxposition(self, letra):
        char = list('abcdefghijklmnñopqrstuvwxyz')
        return char.index(letra)

    def positionxnumber(self, number):
        char = list('abcdefghijklmnñopqrstuvwxyz')
        return char[number]

    def encrypted_char(self, sum):
        division = divmod(sum, 27)
        if division[0] == 0:
            return sum
        else:
            return division[1]


if __name__ == '__main__':
    Autoclave().arguments()
