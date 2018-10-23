from django.shortcuts import render
from django.template import Template, Context
from django.template.loader import get_template, render_to_string
from django.http import HttpResponse
import datetime

def main(request):
    template = get_template('main/index.html')
    context = {
        'title': 'Лиственница с берегов Байкала в Санкт-Петербурге',
        'subtitle': 'Пиломатериалы из лиственницы от производителя по низкой цене',
        'text': [
            ''' 
                На берегах Байкала в экологически чистых условиях произрастает лиственница сибирская. Древесина этого дерева красива и уникальна.
                Главные её качества — это прочность, твердость и невероятная стойкость против гниения, что
                особенно важно в строительстве. С годами лиственничная древесина становится только прочнее.
                Не зря это дерево сравнивают с камнем. В Венеции, которая стоит на воде, сваи домов сделаны
                из лиственницы. Большая влажность только укрепляет этот необыкновенный строительный материал.
                Кстати, Петербург тоже не обошелся без знаменитой сибирской лиственницы.
            ''',
            '''
                Лиственница, используемая при строительстве дома, выделяет особые полезные вещества - фитонциды, которые через кожу и легкие
                способны благоприятно влиять на организм человека. Фитонциды останавливают рост болезнетворных
                бактерий и грибов, нормализуют артериальное давление и сердечный ритм, активируют нервную
                и иммунную систему человека.
            ''',
            '''
                В доме из лиственницы вам будет комфортно: тепло зимой и прохладно летом.
            '''
        ],
        'subsubtitle': 'Мы предлагаем Вам древесину лиственницы только экстра и прима сортов',
        'subsubtext': 'У Вас будет уникальная возможность использовать такую же древесину, какую отправляют на экспорт в Европу',
        'advantages': {
            'КРАСИВО И ПОЛЕЗНО ДЛЯ ЗДОРОВЬЯ': '''
                    Дома из лиственницы очень красивы и обладают высокой прочностью, 
                    так как устойчивы к гниению, образованию плесени и грибка.
                    Фитонциды, которые выделяет это дерево, останавливают рост микроорганизмов 
                    и бактерий, а значит, ваши дети будут меньше болеть
                ''',
            'ТЕПЛО': '''
                    Дома из лиственницы лучше сохраняют тепло зимой, а летом в них достаточно прохладно
                ''',
            'БЕЗОПАСНО': '''
                    Дома из лиственницы отличаются высокой огнеупорностью, которая превышает огнестойкость сосновых пород в два раза
                '''
        }
    }
    response_string = template.render(context)

    return HttpResponse(response_string)


def contacts(request):
    context = {
        'title': 'О нас',
        'contacts': {
            'Город': 'Санкт-Петербург',
            'Телефон': '+79119697705',
            'Электронная почта': 'sibles.spb@yandex.ru'
        }
    }
    response_string = render_to_string(
        'main/contacts.html',
        context
    )
    return HttpResponse(response_string)   


def catalog(request):
    context = {
        'title': 'Каталог',
        'subtitle': 'Сибирская (ангарская) лиственница — хороший выбор для создания дома вашей мечты',
        'text': [
            '''
                Из имеющихся у нас различных пиломатериалов Вы можете сделать как стены (внутренняя и внешняя обшивка), так и потолок и пол.
                Отлично подойдет для дома, бани, террасы или беседки. Доска лиственницы очень прочная, Вы всегда будете
                уверенны, что ни перепад температур, ни влажность, ни годы ей не страшны. А приятный рисунок и многообразие
                оттенков этой породы достоины того, чтобы не прятать его за краской, а гордо показать, например, под
                лаком, расположив панели в любом направлении по Вашему желанию.
            ''',
            '''
                Лиственница — это всегда экологично, всегда безопасно, всегда красиво.
            '''
        ]
    }
    return render(request, 'main/catalog.html', context)


def services(request):
    context = {
        'title': 'Услуги',
        'subtitle': 'Вам нужна профессиональная строительная бригада в Санкт-Петербурге?',
        'text': [
            ''' 
                Наши высококвалифицированные специалисты помогут смонтировать конструкции любой сложности.
                Работы по монтированию стен и полов. Ремонтные работы. Мы учитываем пожелания наших клиентов 
            ''',
            '''
                Воплотим Ваши идеи качественно и в срок
            '''
        ]
    }
    return render(request, 'main/services.html', context)


def about(request):
    context = {
        'title': 'О нас',
        'about_text': '''
                Мы занимаемся доставкой пиломатериалов из лиственницы в Санкт-Петербург напрямую с берегов Байкала,
                 а также перевозкой её по СПб и Ленобласти.
            ''',
        'about_text_order': 'Заказать пиломатериалы оптом или услугу строительной бригады без посредников можно по телефону',
        'phone_number': '+79119697705'
    }
    return render(request, 'main/about.html', context)
