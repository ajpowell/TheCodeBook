#
# Text analysis shows that X -> e as most common letter in English
# From there can start to guess other letters JPX is likely to be 'the'
# and work from there to fill the string of translated characters.
#
#
# key = 'ciovyblkftqmadzhpsjnurgewx'
#
# End of text reveals answer:
#
# 'the first codeword is othello.'
#
# So, the answer is 'OTHELLO'
#
text = """
BT JPX RMLX PCUV AMLX ICVJP IBTWXVR CI M LMT'R PMTN, MTN
YVCJX CDXV MWMBTRJ JPX AMTNGXRJBAH UQCT JPX QGMRJXV CI JPX
YMGG CI JPX HBTW'R QMGMAX; MTN JPX HBTW RMY JPX QMVJ CI JPX
PMTN JPMJ YVCJX. JPXT JPX HBTW'R ACUTJXTMTAX YMR APMTWXN,
MTN PBR JPCUWPJR JVCUFGXN PBL, RC JPMJ JPX SCBTJR CI PBR
GCBTR YXVX GCCRXN, MTN PBR HTXXR RLCJX CTX MWMBTRJ
MTCJPXV. JPX HBTW AVBXN MGCUN JC FVBTW BT JPX MRJVCGCWXVR,
JPX APMGNXMTR, MTN JPX RCCJPRMEXVR. MTN JPX HBTW RQMHX,
MTN RMBN JC JPX YBRX LXT CI FMFEGCT, YPCRCXDXV RPMGG VXMN
JPBR YVBJBTW, MTN RPCY LX JPX BTJXVQVXJMJBCT JPXVXCI,
RPMGG FX AGCJPXN YBJP RAMVGXJ, MTN PMDX M APMBT CI WCGN
MFCUJ PBR TXAH, MTN RPMGG FX JPX JPBVN VUGXV BT JPX
HBTWNCL. JPXT AMLX BT MGG JPX HBTW'R YBRX LXT; FUJ JPXE
ACUGN TCJ VXMN JPX YVBJBTW, TCV LMHX HTCYT JC JPX HBTW JPX
BTJXVQVXJMJBCT JPXVXCI. JPXT YMR HBTW FXGRPMOOMV WVXMJGE
JVCUFGXN, MTN PBR ACUTJXTMTAX YMR APMTWXN BT PBL, MTN PBR
GCVNR YXVX MRJCTBRPXN. TCY JPX KUXXT, FE VXMRCT CI JPX
YCVNR CI JPX HBTW MTN PBR GCVNR, AMLX BTJC JPX FMTKUXJ
PCURX; MTN JPX KUXXT RQMHX MTN RMBN, C HBTW, GBDX ICVXDXV;
GXJ TCJ JPE JPCUWPJR JVCUFGX JPXX, TCV GXJ JPE ACUTJXTMTAX
FX APMTWXN; JPXVX BR M LMT BT JPE HBTWNCL, BT YPCL BR JPX
RQBVBJ CI JPX PCGE WCNR; MTN BT JPX NMER CI JPE IMJPXV
GBWPJ MTN UTNXVRJMTNBTW MTN YBRNCL, GBHX JPX YBRNCL CI JPX
WCNR, YMR ICUTN BT PBL; YPCL JPX HBTW TXFUAPMNTXOOMV JPE
IMJPXV, JPX HBTW, B RME, JPE IMJPXV, LMNX LMRJXV CI JPX
LMWBABMTR, MRJVCGCWXVR, APMGNXMTR, MTN RCCJPRMEXVR;
ICVMRLUAP MR MT XZAXGGXTJ RQBVBJ, MTN HTCYGXNWX, MTN
UTNXVRJMTNBTW, BTJXVQVXJBTW CI NVXMLR, MTN RPCYBTW CI PMVN
RXTJXTAXR, MTN NBRRCGDBTW CI NCUFJR, YXVX ICUTN BT JPX
RMLX NMTBXG, YPCL JPX HBTW TMLXN FXGJXRPMOOMV; TCY GXJ
NMTBXG FX AMGGXN, MTN PX YBGG RPCY JPX BTJXVQVXJMJBCT. JPX
IBVRJ ACNXYCVN BR CJPXGGC.
"""

# text = 'AAAAABBBBBZZZZZ'

def analyse(cipher_text):
    letter_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    letter_count_total = 0
    for character in cipher_text:
        dat = ord(character)
        if dat >= 65 and dat <=90:
            letter_count_total = letter_count_total + 1
            letter_count[dat - 65] = letter_count[dat - 65] + 1
    
    print('letter_count_total = {}'.format(letter_count_total))

    for n in range(len(letter_count)):
        print('{} -> {:0.1f} [{}]'.format(chr(n + 65), ((letter_count[n]* 1.0)/letter_count_total)*100.0, letter_count[n]))


def decode(cipher_text, key):
    # Display the text using the key supplied
    if len(key) != 26:
        print('ERROR: key is not of the correct length')
    else:
        output = ''
        for character in cipher_text:
            dat = ord(character)
            if dat >= 65 and dat <=90:
                # convert using the key
                decoded_character = key[dat - 65:dat - 65 + 1]
                if decoded_character != '.':
                    output = output + decoded_character
                else:
                    output = output + character
            else:
                output = output + character
        
        print(output)

def main():
    analyse(text)

    #     'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = '..........................'
    key = 'ciovyblkftqmadzhpsjnurgewx'
    decode(text, key)


if __name__ == "__main__":
    # Jump to main code
    main()
