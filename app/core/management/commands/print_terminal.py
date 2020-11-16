from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('text', type=str,help='type anything on terminal')
    
    def handle(self,*arg,**options):
        hi=options['text']
        self.stdout.write(hi)