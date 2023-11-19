from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange


# Formulário para selecionar o tipo de classificador (tela inicial)
class ClassifierForm(FlaskForm):
    classifier = SelectField('Escolha o Classificador:', choices=[
        ('KNN', 'KNN'),
        ('SVM', 'SVM'),
        ('MLP', 'MLP'),
        ('DT', 'Decision Tree'),
        ('RF', 'Random Forest')
    ])
    submit = SubmitField('Treinar')


# Formulário com os campos do classificador KNN
class KNNForm(FlaskForm):
    n_neighbors = IntegerField('Número de Vizinhos', validators=[DataRequired(), NumberRange(min=1)])


# Formulário com os campos do classificador SVM
class SVMForm(FlaskForm):
    # C = FloatField('C (Regularização)', validators=[DataRequired()])
    kernel = SelectField('Kernel', choices=[('linear', 'Linear'), ('rbf', 'RBF'), ('poly', 'Polinomial')])
    degree = IntegerField('Grau (para kernel polinomial)', validators=[NumberRange(min=1)], default=3)


# Formulário com os campos do classificador MLP
class MLPForm(FlaskForm):
    hidden_layer_sizes = StringField('Tamanhos das Camadas Ocultas (e.g. 10,10)', validators=[DataRequired()])
    max_iter = IntegerField('Número Máximo de Iterações', validators=[DataRequired(), NumberRange(min=1)])


# Formulário com os campos do classificador Decision Tree
class DTForm(FlaskForm):
    max_depth = IntegerField('Profundidade Máxima', validators=[NumberRange(min=1)])


# Formulário com os campos do classificador Random Forest
class RFForm(FlaskForm):
    n_estimators = IntegerField('Número de Árvores', validators=[DataRequired(), NumberRange(min=1)])
    max_depth = IntegerField('Profundidade Máxima', validators=[NumberRange(min=1)], default=None)
