"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install -e .`
- Use the same interpreter as the one used to install the bot (`pip install -e .`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""

from botcity.core import DesktopBot
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *


class Bot(DesktopBot):
    def action(self, execution=None):
        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id

        # Teste de abrir e preencher no browser
        self.browse("https://www.hashtagtreinamentos.com/")
        
        if not self.find( "click_1", matching=0.97, waiting_time=10000):
            self.not_found("click_1")
        self.click()
        
        if not self.find( "pagina_carregou", matching=0.97, waiting_time=10000):
            self.not_found("pagina_carregou")
        
        
        self.scroll_down(3800)
        
        
        if not self.find( "nome", matching=0.97, waiting_time=10000):
            self.not_found("nome")
        self.click()
        
        self.paste('Arthur')
        
        
        if not self.find( "email", matching=0.97, waiting_time=10000):
            self.not_found("email")
        self.click()
        
        
        self.paste('teste@gmail.com')
        
        if not self.find( "botao", matching=0.97, waiting_time=10000):
            self.not_found("botao")
        self.click()
        
        

        # Uncomment to mark this task as finished on BotMaestro
        # self.maestro.finish_task(
        #     task_id=execution.task_id,
        #     status=AutomationTaskFinishStatus.SUCCESS,
        #     message="Task Finished OK."
        # )

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()
