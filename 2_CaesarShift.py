#
# Brute force approach to decrypting the cipher text i.e. all 26 possiblities and then
# visual inspection to find solution.
#
# Decrypts to Latin:
#
#   19 - FABER EST SUAE QUISQUE FORTUNAE APPIUS CLAUDIUS CAECUS DICTUM ARCANUM EST NEUTRON
#
#   APPIUS CLAUDIUS THE BLIND SAID THE SECRET IS THE NEUTRON
#
# So, the answer is 'NEUTRON'
#

cipher_text = 'MHILY LZA ZBHL XBPZXBL MVYABUHL HWWPBZ JSHBKPBZ JHLJBZ KPJABT HYJHUBT LZA ULBAYVU'

def shiftByN(text, n):
    text_length = len(text)
    # print(text_length)
    output = ''

    for i in range(text_length):
        orig_ord = ord(text[i:i+1])
        if orig_ord == 32:
            # Allow spaces to pass-through...
            output = output + ' '
        else:
            new_ord = orig_ord + n
            if new_ord > 90:
                new_ord = new_ord - 26
            # print('{}[{}] -> {}[{}]'.format(orig_ord, chr(orig_ord), new_ord, chr(new_ord)))

            output = output + chr(new_ord)

    return output


def main():
    print(cipher_text)
    for n in range(26):
        plain_text = shiftByN(cipher_text, n+1)

        print('{} - {}'.format(n+1, plain_text))


if __name__ == "__main__":
    # Jump to main code
    main()
