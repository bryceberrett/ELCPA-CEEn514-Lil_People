from tethys_sdk.base import TethysAppBase, url_map_maker


class LilPeopleElcpa(TethysAppBase):
    """
    Tethys app class for Evacuation Least Cost Path App.
    """

    name = 'Evacuation Least Cost Path App'
    index = 'lil_people_elcpa:home'
    icon = 'lil_people_elcpa/images/200px-The_Great_Wave_off_Kanagawa_-_wave.jpg'
    package = 'lil_people_elcpa'
    root_url = 'lil-people-elcpa'
    color = '#c0392b'
    description = 'This app uses a least cost path analysis to determine the best routes for evacuation based on weighted variables.'
    tags = '"Evacuation","Least-cost"'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='lil-people-elcpa',
                controller='lil_people_elcpa.controllers.home'
            ),
            UrlMap(
                name='PProp',
                url='lil-people-elcpa/PProp',
                controller='lil_people_elcpa.controllers.PProp'
            ),
        )

        return url_maps

