from django.core.management import BaseCommand

from new_app.models import Student


class Command(BaseCommand):

    def handle(self, *args, **options):
        student_list = [
            {'last_name': 'Ivanov', 'first_name': 'Oleg'},
            {'last_name': 'Petrov', 'first_name': 'Petr'},
            {'last_name': 'Alexandrov', 'first_name': 'Vlad'},
            {'last_name': 'Andreev', 'first_name': 'Maxim'},
        ]

        # for student_item in student_list:
        #     Student.objects.create(**student_item)

        students_for_create = []
        for student_item in student_list:
            students_for_create.append(
                Student(**student_item)
            )

        Student.objects.bulk_create(students_for_create)
        # пакетное добавление,
        # т.о. не на каждую итерацию цикла for вызывается create, а один раз вызывается. Благодаря пакетному добавлению
