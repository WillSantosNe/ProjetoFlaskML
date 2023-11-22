import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


"""
Carrega dataset no formato CSV
Seleciona colunas utilizadas no Machine Learning

Retorna o "X" e "y"
"""
def carregar_dados():
    df = pd.read_csv("uploads/diabetes.csv")
    colunas_atributos = ['Age', 'Sex', 'BMI', 'CholCheck']
    X = df[colunas_atributos]
    y = df['Diabetes_binary']
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(y)
    return X, y



"""
Realiza o treinamento de acordo com o classificador recebido no parâmetro
Realiza plotagem de matrix de confusão e transforma imagem
Salva imagem na pasta static com o nome de acordo com o classificador

Retorna o nome do arquivo de imagem salvo
"""
def treinar_e_avaliar(classificador, parametros, X_train, y_train, X_test, y_test):
    if classificador == 'KNN':
        clf = KNeighborsClassifier(
            n_neighbors=parametros['n_neighbors'],
            weights=parametros['weights'],
            algorithm=parametros['algorithm']
        )
    elif classificador == 'SVM':
        clf = SVC(
            kernel=parametros['kernel'],
            degree=parametros['degree'],
            C=parametros['C'],
            gamma=parametros['gamma']
        )
    elif classificador == 'MLP':
        clf = MLPClassifier(
            hidden_layer_sizes=parametros['hidden_layer_sizes'],
            max_iter=parametros['max_iter'],
            learning_rate_init=parametros['learning_rate_init'],
            solver=parametros['solver']
        )
    elif classificador == 'DT':
        clf = DecisionTreeClassifier(
            max_depth=parametros['max_depth'],
            criterion=parametros['criterion'],
            min_samples_split=parametros['min_samples_split']
        )
    elif classificador == 'RF':
        clf = RandomForestClassifier(
            n_estimators=parametros['n_estimators'],
            max_depth=parametros['max_depth'],
            criterion=parametros['criterion'],
            min_samples_split=parametros['min_samples_split']
        )
    else:
        raise ValueError("Classificador não encontrado.")
    
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    matriz_confusao = confusion_matrix(y_test, y_pred)
    
    # Salvando a matriz de confusão como imagem
    nome_imagem = f'confusion_matrix_{classificador}.png'
    caminho_imagem = f'static/{nome_imagem}'
    disp = ConfusionMatrixDisplay(confusion_matrix=matriz_confusao)
    fig, ax = plt.subplots(figsize=(6,6))
    disp.plot(ax=ax)
    plt.savefig(caminho_imagem)
    plt.close(fig)

    return nome_imagem



carregar_dados()
