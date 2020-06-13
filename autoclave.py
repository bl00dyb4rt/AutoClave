#!/usr/bin/env python3
import argparse
import subprocess
from pprint import pprint
import time
from alive_progress import alive_bar, config_handler


class Autoclave:

    def arguments(self):
        cipher_parse = argparse.ArgumentParser(description='Encrypt and Decrypt words', add_help=True)

        cipher_parse.add_argument('-w', '--word', dest='word', action='store',
                                  help='word to encrypt', required=True)
        cipher_parse.add_argument('-k', '--key', dest='key', action='store',
                                  help='key', required=True)
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

            final_key = self.generate_key_from_password(word, key)
            final_text = self.generate_encoded_word(word, final_key)
            subprocess.run(['echo', "\n Original word : " + final_key.upper()])
            subprocess.run(['echo', "\n Encrypted Word : " + final_text.upper()])


        else:
            subprocess.run(['echo', 'Decrypt....! \n'])

    def vigeniere_list(self):
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

    def generate_encoded_word(self, message, key):
        vigeniere_list = self.vigeniere_list()
        final_list = []
        final_word = ''
        for i in range(len(message)):
            final_list.append([int(vigeniere_list[0].index(message[i])), int(vigeniere_list[0].index(key[i]))])
        for f in final_list:
            final_word += vigeniere_list[f[0]][f[1]]
        return final_word

    def generate_key_from_password(self, message, password):
        length_key = len(message) - len(password)
        final_message = ''
        for i in range(length_key):
            final_message += message[i]
        return password + final_message


if __name__ == '__main__':
    Autoclave().arguments()
