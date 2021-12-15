from django import forms
from django.forms import modelformset_factory

class IdeaCaptureForm(forms.Form):

    # help text
    labels = ['Idea title', 'Aim', 'Objectives', 'Description', 'Tasks']
    help_title = 'title help'
    help_aim = 'aim help'
    help_objectives = 'objectives help'
    help_idea_description = 'idea description help'
    help_tasks = 'idea description help'

    idea_title = forms.CharField(label=labels[0], widget=forms.Textarea(attrs={'rows': '1', 'cols': '60','size': '40'}), help_text=help_title)
    aim = forms.CharField(label=labels[1], widget=forms.Textarea(attrs={'rows': '2'}), help_text=help_aim)
    objectives = forms.CharField(label=labels[2], initial='>\n>\n>', widget=forms.Textarea(attrs={'rows': '3'}), help_text=help_objectives)
    idea_description = forms.CharField(label=labels[3], widget=forms.Textarea(attrs={'rows': '4'}), help_text=help_idea_description)
    tasks = forms.CharField(label=labels[4], widget=forms.Textarea(attrs={'rows': '4'}), help_text=help_tasks)


class DocCapture(forms.Form):
    #empty_layer_name = forms.CharField(max_length=255, required=True, label="Name of new Layer")
    #my_in = forms.CharField(label='lab')
    #fieldsNew = forms.IntegerField(label='fields')
    #total_input_fields = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):

        extra_fields = kwargs.pop('extra', 0)

        # check if extra_fields exist. If they don't exist assign 0 to them
        if not extra_fields:
            extra_fields = 0

        super(DocCapture, self).__init__(*args, **kwargs)
        #self.fields['total_input_fields'].initial = extra_fields

        for index in range(int(extra_fields)):
            # generate extra fields in the number specified via extra_fields
            #self.fields['Chapter_{index}'.format(index=index + 1)] = forms.CharField(required=False)
            self.fields['Chapter_{index}'.format(index=index+1)] = forms.CharField(required=False)
            self.fields['Description_{index}'.format(index=index + 1)] = forms.CharField(required=False, label='desc')









