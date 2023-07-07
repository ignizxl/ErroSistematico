import sig

AMARELOR = 0.32
AMARELOG = 0.25
AMARELOB = 0.09

def TOINT(A):
    return int(round((A) * 100.0))

AMARELOR, sigAmareloR = sig.calculos(sig.amareloR)

AMARELOG, sigAmareloG = sig.calculos(sig.amareloG)

AMARELOB, sigAmareloB = sig.calculos(sig.amareloB)
try:
    while True:
        for i in range(len(sig.amareloR)):
            if ((TOINT(AMARELOR - 5 * sigAmareloR) <= TOINT(sig.amareloR[i])
                and TOINT(sig.amareloR[i]) <= TOINT(AMARELOR + 5 * sigAmareloR))
                and (TOINT(AMARELOG - 5 * sigAmareloG) <= TOINT(sig.amareloG[i])
                and TOINT(sig.amareloG[i]) <= TOINT(AMARELOG + 5 * sigAmareloG))
                and (TOINT(AMARELOB - 5 * sigAmareloB) <= TOINT(sig.amareloB[i])
                and TOINT(sig.amareloB[i]) <= TOINT(AMARELOB + 5 * sigAmareloB))):
                print("AMARELO")
                print("VERMELHO")
            else:
                print("DESCONHECIDA")
        break
except EOFError:
    pass
