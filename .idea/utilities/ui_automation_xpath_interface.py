"""
to store xpaths of UI elements from different Ui sections like designer , object browser etc..

"""

class AppLoginPage():

    x1 = '//div'
    search_text = '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input'


class PpMainPage():
    help_center1 = '//div[@title="Get help for Pipeline Pilot Professional Client"]'
    help_center ='/html/body/div[2]/div[2]/p[1]/a'
    install_upgrade_client = '/html/body/div[2]/div[2]/p[2]/a'
    webport = '/html/body/div[2]/div[7]/p/a'


    class HelpCenter():

        getting_started = '/html/body/div/div[2]/div[1]/a[1]/img'
        pp ='/html/body/div/div[2]/div[1]/a[1]/img'
        administrator = "//table//div[@title='Help Center resources for administrators']"
        admin2='/html/body/table/tbody/tr[1]/td[1]/div[2]/a'
        advanced_search='/html/body/div[2]/p/a[1]'

class LIMS():
    xpa ='/html/'
