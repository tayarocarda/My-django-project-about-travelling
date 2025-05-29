from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='pages/', verbose_name='Изображение')),
                ('meta_description', models.CharField(blank=True, help_text='Краткое описание для поисковых систем', max_length=200, verbose_name='Meta описание')),
                ('keywords', models.CharField(blank=True, help_text='Ключевые слова через запятую', max_length=200, verbose_name='Ключевые слова')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('order', models.IntegerField(default=0, verbose_name='Порядок')),
            ],
            options={
                'verbose_name': 'Страница',
                'verbose_name_plural': 'Страницы',
                'ordering': ['order', 'title'],
            },
        ),
        migrations.CreateModel(
            name='ContentCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('icon', models.CharField(help_text='Название иконки из Material Icons (например: person, school, groups)', max_length=50, verbose_name='Иконка Material Icons')),
                ('slug', models.SlugField(help_text='Уникальный идентификатор для URL (например: about-me, my-program)', unique=True, verbose_name='URL')),
                ('order', models.IntegerField(default=0, verbose_name='Порядок отображения')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активно')),
            ],
            options={
                'verbose_name': 'Карточка контента',
                'verbose_name_plural': 'Карточки контента',
                'ordering': ['order', 'title'],
            },
        ),
        migrations.CreateModel(
            name='AcademicSupervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='ФИО')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='staff/', verbose_name='Фото')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Электронка')),
                ('page', models.OneToOneField(help_text="Страница 'Менеджмент', к которой относится этот руководитель", on_delete=models.deletion.CASCADE, related_name='academic_supervisor', to='app2.page')),
            ],
            options={
                'verbose_name': 'Академический руководитель',
                'verbose_name_plural': 'Академические руководители',
            },
        ),
        migrations.CreateModel(
            name='ProgramManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='ФИО')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='staff/', verbose_name='Фото')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Электронка')),
                ('order', models.PositiveIntegerField(db_index=True, default=0, verbose_name='Порядок')),
                ('page', models.ForeignKey(help_text="Страница 'Менеджмент', к которой относятся эти менеджеры", on_delete=models.deletion.CASCADE, related_name='program_managers', to='app2.page')),
            ],
            options={
                'verbose_name': 'Менеджер программы',
                'verbose_name_plural': 'Менеджеры программы',
                'ordering': ['order', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Classmate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Полное имя или как вы его называете', max_length=200, verbose_name='ФИО / Имя')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='classmates/', verbose_name='Фото')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Электронка')),
                ('phone', models.CharField(blank=True, max_length=50, verbose_name='Телефон')),
                ('order', models.PositiveIntegerField(db_index=True, default=0, verbose_name='Порядок')),
                ('page', models.ForeignKey(help_text="Страница 'Мои сокурсники', к которой относятся эти сокурсники", on_delete=models.deletion.CASCADE, related_name='classmates', to='app2.page')),
            ],
            options={
                'verbose_name': 'Сокурсник',
                'verbose_name_plural': 'Сокурсники',
                'ordering': ['order', 'name'],
            },
        ),
    ] 