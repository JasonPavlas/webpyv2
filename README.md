# webpyv2

Got to here * in the Writing your first Django app, part 3 django demo. 
https://docs.djangoproject.com/en/4.1/intro/tutorial03/

* = 
<h1>{{ question.question_text }}</h1>
<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>