from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models


# Create your models here.

class Category(models.Model):
    category_title = models.CharField(
        verbose_name='カテゴリ',
        max_length=20
    )

    def __str__(self):
        '''オブジェクトを文字列に変換して返す

        :return: （カテゴリ名）
        '''
        return self.category_title


class Question(models.Model):
    question_category = models.ForeignKey(
        Category,

        verbose_name='カテゴリ',

        on_delete=models.PROTECT
    )

    question = models.TextField('問題文', blank=True)

    create_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  verbose_name="投稿者",
                                  on_delete=models.CASCADE)
    answer = models.CharField('正解', max_length=128)
    create_at = models.DateTimeField('投稿日', auto_now_add=True)

    def __str__(self):
        return self.question


class Question2(models.Model):
    question_category = models.ForeignKey(
        Category,

        verbose_name='カテゴリ',

        on_delete=models.PROTECT
    )
    question = models.TextField('問題文', blank=True)

    create_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  verbose_name="投稿者",
                                  on_delete=models.CASCADE)
    answer = models.CharField('正解', max_length=128)
    create_at = models.DateTimeField('投稿日', auto_now_add=True)

    def __str__(self):
        return self.question


class Question3(models.Model):
    question_category = models.ForeignKey(
        Category,

        verbose_name='カテゴリ',

        on_delete=models.PROTECT
    )
    question = models.TextField('問題文', blank=True)

    create_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  verbose_name="投稿者",
                                  on_delete=models.CASCADE)
    answer = models.CharField('正解', max_length=128)
    create_at = models.DateTimeField('投稿日', auto_now_add=True)

    def __str__(self):
        return self.question


class Question4(models.Model):
    question_category = models.ForeignKey(
        Category,

        verbose_name='カテゴリ',

        on_delete=models.PROTECT
    )
    question = models.TextField('問題文', blank=True)

    create_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  verbose_name="投稿者",
                                  on_delete=models.CASCADE)
    answer = models.CharField('正解', max_length=128)
    create_at = models.DateTimeField('投稿日', auto_now_add=True)

    def __str__(self):
        return self.question


class Question5(models.Model):
    question_category = models.ForeignKey(
        Category,

        verbose_name='カテゴリ',

        on_delete=models.PROTECT
    )
    question = models.TextField('問題文', blank=True)

    create_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  verbose_name="投稿者",
                                  on_delete=models.CASCADE)
    answer = models.CharField('正解', max_length=128)
    create_at = models.DateTimeField('投稿日', auto_now_add=True)

    def __str__(self):
        return self.question


class Choice(models.Model):
    choice_category = models.ForeignKey(
        Category,

        verbose_name='カテゴリ',

        on_delete=models.PROTECT
    ),

    choice_to = models.ForeignKey(Question, verbose_name="問題文",
                                  on_delete=models.CASCADE)
    fault = models.CharField('不正解1', max_length=128)

    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.fault


class Choice2(models.Model):
    choice_category = models.ForeignKey(
        Category,

        verbose_name='カテゴリ',

        on_delete=models.PROTECT
    ),

    choice_to = models.ForeignKey(Question2, verbose_name="問題文",
                                  on_delete=models.CASCADE)
    fault = models.CharField('不正解1', max_length=128)

    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.fault


class Choice3(models.Model):
    choice_category = models.ForeignKey(
        Category,

        verbose_name='カテゴリ',

        on_delete=models.PROTECT
    ),

    choice_to = models.ForeignKey(Question3, verbose_name="問題文",
                                  on_delete=models.CASCADE)
    fault = models.CharField('不正解1', max_length=128)

    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.fault


class Choice4(models.Model):
    choice_category = models.ForeignKey(
        Category,

        verbose_name='カテゴリ',

        on_delete=models.PROTECT
    ),

    choice_to = models.ForeignKey(Question4, verbose_name="問題文",
                                  on_delete=models.CASCADE)
    fault = models.CharField('不正解1', max_length=128)

    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.fault


class Choice5(models.Model):
    choice_category = models.ForeignKey(
        Category,

        verbose_name='カテゴリ',

        on_delete=models.PROTECT
    ),

    choice_to = models.ForeignKey(Question5, verbose_name="問題文",
                                  on_delete=models.CASCADE)
    fault = models.CharField('不正解1', max_length=128)

    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.fault


class QuizResult(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             verbose_name="回答者",
                             on_delete=models.CASCADE)  # ユーザー情報
    genre = models.ForeignKey(Category, verbose_name="カテゴリ", on_delete=models.CASCADE)  # ジャンル
    correct_count = models.CharField('スコア', max_length=128)  # 正解数
    timestamp = models.DateTimeField(auto_now_add=True)  # タイムスタンプ

    def __str__(self):
        return self.correct_count
