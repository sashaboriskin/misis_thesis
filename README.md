# Исследование возможностей адаптивного вызова контекста с целью повышения точности ответа и снижение вычислительной нагрузки

## Обзор проекта
Данный проект исследует эффективность двухэтапного генеративного подхода к адаптивному поиску и генерации (Retrieval-Augmented Generation, RAG) для улучшения точности ответов языковых моделей. Ключевая идея заключается в использовании активаций нейронной сети для предсказания необходимости обращения к внешним источникам данных.

## Основные компоненты

### Наборы данных
Проект использует четыре набора данных:
- NaturalQuestions (NQ)
- 2WikiMultiHopQA (Wiki)
- HotpotQA
- MuSiQue

### Модели
- **Базовая модель**: Llama-3.1-8B-Instruct
- **Классификаторы**: LogisticRegression, CatBoost

### Метрики оценки
- F1
- Exact Match (EM)
- InAcc
- BLEU
- ROUGE

## Методология
1. **Предварительная обработка данных**: Генерация ответов в трех режимах (без контекста, с контекстом, DOLA)
2. **Извлечение активаций**: Сбор активаций нейронной сети на разных слоях (2, 12, 28, 31)
3. **Обучение классификаторов**: Использование активаций для предсказания необходимости RAG
4. **Оценка производительности**: Сравнение с базовыми подходами "Always RAG" и "Never RAG"

## Структура проекта
- `dataset.py` - загрузка и обработка данных
- `metrics.py` - функции для вычисления метрик качества
- `prompts.py` - шаблоны запросов для модели
- `config.yaml` - конфигурация параметров проекта
- `2stage_forward.ipynb` - основной исполняемый ноутбук

## Результаты
Эксперименты показывают, что двухэтапный подход позволяет значительно улучшить точность ответов по сравнению с базовыми стратегиями, особенно на сложных многоэтапных запросах.

## Использование
1. Установите зависимости
2. Настройте конфигурацию в `config.yaml`
3. Запустите `2stage_forward.ipynb` для воспроизведения экспериментов
