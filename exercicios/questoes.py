
import multiprocessing
import threading
import time
from concurrent.futures.process import ProcessPoolExecutor

from os.path import isfile, join
import random

import psutil, subprocess, os
import tqdm as tqdm


def rodar(func):
    if __name__ == '__main__':
        print('-' * 10, func.__name__, '-' * 10)
        func()


@rodar
def questao01():
    processos = []
    for proc in psutil.process_iter():
        obj = {
            "Nº pid": proc.pid,
            "Nome": proc.name(),
            "Uso Memoria": "{:.0%}".format(proc.memory_percent().real)
        }
        processos.append(obj)

    for i in range(len(processos)):
        m = processos[i]
        p = psutil.Process(m['Nº pid'])
        uso = p.cpu_percent(interval=0.1)
        m.update({"Uso CPU": uso})

        print(m)


def questao02():
    nome_arquivo = input("Escreva o nome do arquivo :")

    caminho = 'C:/Users/Asus/Desktop/' + nome_arquivo
    executavel = f"notepad.exe {caminho}"

    os.system(executavel)


def questao03():
    try:
        diretorio = input("Entre com o caminho do diretório : ")
        arquivos = [f for f in os.listdir(diretorio)]
        arq = []
        for i in arquivos:
            nome_aqr = i
            tamanho_arq = os.path.getsize(join(diretorio, i))

            arq.append((nome_aqr, str(tamanho_arq)))

        sorted_arq = sorted(arq, key=lambda item: item[1])

        with open('sorted_list.txt', 'w') as f:
            for x in sorted_arq:
                f.write(str(x) + "\n")
            f.close()

    except Exception as erro:
        print(str(erro))


def questao04():
    try:
        for l in reversed(open("arquivo.txt").readlines()):
            r = l[::-1]
            print(r)

    except Exception as erro:
        print(erro)


def questao05():
    a = open('a.txt', 'r')
    b = open('b.txt', 'r')

    lista_a = a.read().split(" ")
    lista_b = b.read().split(" ")
    a.close()
    b.close()

    soma = 0
    k = [float(j) for j in lista_a]
    l = [float(i) for i in lista_b]

    for t, v in zip(k, l):
        soma += t + v

    print(soma)


def fatorial(n):
    fat = n
    for i in range(n - 1, 1, -1):
        fat = fat * i
    return fat


def num_aleatorio(qtd):
    minimo = 2
    maximo = 10
    for i in range(qtd):
        yield random.randint(minimo, maximo)


def sequencial(qtd):
    for num in num_aleatorio(qtd):
        fatorial(num)


def thread4():
    for num in num_aleatorio(1_000_000):
        fatorial(num)
    inicio = time.time()

    threads = []

    for x in tqdm.tqdm(range(4)):
        t = threading.Thread(target=thread4)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
    fim = time.time()

    print(fim - inicio)


def multiprocess():
    manager = multiprocessing.Manager()
    lista = manager.list()

    inicio = time.time()

    with ProcessPoolExecutor(max_workers=4) as executor:
        for i in range(30):
            future = executor.submit(sequencial, i, lista)
        fim = time.time()

    print(inicio - fim)


if __name__ == "__main__":
    pass
