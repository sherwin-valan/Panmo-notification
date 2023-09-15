from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import FormView
from django.core.mail import send_mail

from .models import Experiment
from .forms import EmailForm

class ExperimentCheckView(FormView):
    template_name = 'polls/experiment_check_modal.html'
    form_class = EmailForm
    success_url = '/thank_you/'

    def form_valid(self, form):
        pk = self.kwargs['pk']
        experiment = Experiment.objects.get(pk=pk)
        experiment.checked = True
        experiment.save()
        
        subject = 'Experiment Checked Off'
        message = f'The experiment "{experiment.name}" has been checked off.'
        from_email = 'your@email.com'
        recipient_list = [form.cleaned_data['customer_email']]

        send_mail(subject, message, from_email, recipient_list)

        return super().form_valid(form)
