# -*- coding: utf-8 -*-
"""
Created on 2020-06-12
@author: b4rt
@mail: root.jmn@gmail.com
"""


class Decrypt:

    def decrypt_text(self, message, key):
        message_crypted = message
        position_list = []
        final_word = ''

        for m in range(len(message_crypted)):
            position_list.append([self.numberxposition(message[m]), self.numberxposition(key[m])])
        for i in position_list:
            final_word += (self.mod_calc(i[0], i[1]))
        return final_word

    def recursive_decrypt(self, message, key_pwd):
        message = message.lower()
        key_pwd = key_pwd.lower()
        counter_dec = divmod(int(len(message)), int(len(key_pwd)))
        count = 0
        words_to_decrypt = []
        for i in range(counter_dec[0]):
            message_crypted = message[count:len(key_pwd) + count]

            words_to_decrypt.append(message_crypted)
            count = count + len(key_pwd)

        words_to_decrypt.append(message[count:len(message)])

        decrypted_list = []
        key_pwd_list = []
        acumulate_key=''
        for word in words_to_decrypt:
            decrypted_text = self.decrypt_text(word, key_pwd)
            decrypted_list.append(decrypted_text)
            # reassign
            key_pwd_list.append([word,key_pwd])
            key_pwd = decrypted_text


        return ({
            'decrypted_list': decrypted_list,
            'decrypted_word': ''.join(decrypted_list),
            'key_pwd_list': key_pwd_list
        })

    def numberxposition(self, letra):
        char = list('abcdefghijklmnñopqrstuvwxyz')
        return char.index(letra)

    def mod_calc(self, x, y):
        # print([x,y])
        var = divmod((int(x) - int(y)), 27)[1]
        return self.positionxnumber(var)

    def positionxnumber(self, number):
        char = list('abcdefghijklmnñopqrstuvwxyz')
        return char[number]
