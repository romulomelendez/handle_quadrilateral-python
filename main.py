import quadrilateral as quad

###########################################---MENU BUILDER---###########################################

def set_line(size=50):
    return '-' * size


def header(text):
    print(set_line())
    print(text.center(50))
    print(set_line())


def menu(list):
    header('HISTOGRAM MAIN MENU')
    print('Select the type of image you want to see the histogram:\n')
    c = 1
    for item in list:
        print(f'{c} - {item}')
        c += 1
    print('\n{}'.format(set_line()))


menu(['Show Quad', 'Rotate(30°)', 'Translation', 'Change Scale', 'Exit'])


##########################################################################################################

def switch(caseSelected):

    if caseSelected == 1:
        return quad.handleQuad()
    elif caseSelected == 2:
        return  quad.handleRotate()
    elif caseSelected == 3:
        return quad.handleTranslation()
    elif caseSelected == 4:
        return quad.handleScale()
    elif caseSelected >= 5:
        print('exiting')
        exit()

if __name__ == '__main__':
    caseSelected = int(input())

    switch(caseSelected)