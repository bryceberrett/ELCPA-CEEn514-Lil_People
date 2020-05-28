# from django.shortcuts import render
# from django.shortcuts import reverse
# from tethys_sdk.permissions import login_required
# from tethys_sdk.gizmos import Button

from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from tethys_sdk.permissions import login_required
from tethys_sdk.gizmos import MapView, Button
from tethys_sdk.gizmos import TextInput, DatePicker, SelectInput
from tethys_sdk.workspaces import app_workspace
from tethys_sdk.gizmos import DataTableView
from tethys_sdk.gizmos import MVDraw, MVView
from tethys_sdk.gizmos import MVLayer
@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    save_button = Button(
        display_text='',
        name='save-button',
        icon='glyphicon glyphicon-floppy-disk',
        style='success',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Save'
        }
    )

    edit_button = Button(
        display_text='',
        name='edit-button',
        icon='glyphicon glyphicon-edit',
        style='warning',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Edit'
        }
    )

    remove_button = Button(
        display_text='',
        name='remove-button',
        icon='glyphicon glyphicon-remove',
        style='danger',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Remove'
        }
    )

    previous_button = Button(
        display_text='Previous',
        name='previous-button',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Previous'
        }
    )

    next_button = Button(
        display_text='Next',
        name='next-button',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Next'
        }
    )

    PProp_button = Button(
        display_text='Project Proposal',
        name='Project_Proposal_Button',
        icon='glyphicon glyphicon-plus',
        style='success',
        href=reverse('lil_people_elcpa:PProp'),
    )

    Background_button = Button(
        display_text='Team',
        name='Background_Button',
        icon='glyphicon glyphicon-plus',
        style='success',
        href=reverse('lil_people_elcpa:Background'),
    )

    Team_button = Button(
        display_text='Team',
        name='Team_Button',
        icon='glyphicon glyphicon-plus',
        style='success',
        href=reverse('lil_people_elcpa:Team'),
    )

    Mockups_button = Button(
        display_text='Mockups',
        name='Mockups_Button',
        icon='glyphicon glyphicon-plus',
        style='success',
        href=reverse('lil_people_elcpa:Mockups'),
    )


    context = {
        'save_button': save_button,
        'edit_button': edit_button,
        'remove_button': remove_button,
        'previous_button': previous_button,
        'next_button': next_button,
        'PProp_button' : PProp_button,
        'Background_button': Background_button,
        'Team_button' : Team_button,
        'Mockups_button' : Mockups_button
    }

    return render(request, 'lil_people_elcpa/home.html', context)

@login_required()
def PProp(request):
    """
    Shows our project proposal
    """

    context = {}

    return render(request, 'lil_people_elcpa/PProp.html', context)

@login_required()
def Background(request):
    """
    Controller for the Background Page
    """

    context = {}

    return render(request, 'lil_people_elcpa/Background.html', context)

@login_required()
def Team(request):
    """
    Controller for the Team Page
    """

    context = {}

    return render(request, 'lil_people_elcpa/Team.html', context)

@login_required()
def Mockups(request):
    """
    Controller for the Mockups Page
    """

    context = {}

    return render(request, 'lil_people_elcpa/Mockups.html', context)

@login_required()
def Geoprocessing_Functions(request):
    """
    Controller for the Background Page
    """

    context = {}

    return render(request, 'lil_people_elcpa/Geoprocessing_Functions.html', context)

@login_required()
def Data_Description(request):
    """
    Controller for the Background Page
    """

    context = {}

    return render(request, 'lil_people_elcpa/Data_Description.html', context)

# Added @appworkspace
@login_required()
def Data_Input(request):
    """
    Geoprocessing page
    """

    # Default Values
    LowValue1 = ''
    HighValue1 = ''
    river = ''
    date_built = ''
    location = ''

    # Errors
    LowValue1_error = ''
    HighValue1_error = ''
    river_error = ''
    date_error = ''
    location_error = ''

    # Handle form submission
    if request.POST and 'add-button' in request.POST:
        # Get values
        has_errors = False
        LowValue1 = request.POST.get('LowValue1', None)
        HighValue1 = request.POST.get('HighValue1', None)
        river = request.POST.get('river', None)
        date_built = request.POST.get('date-built', None)
        location = request.POST.get('geometry', None)

        # Validate
        if not LowValue1:
            has_errors = True
            LowValue1_error = 'LowValue1 is required.'

        if not HighValue1:
            has_errors = True
            HighValue1_error = 'HighValue1 is required.'

        if not river:
            has_errors = True
            river_error = 'River is required.'

        if not date_built:
            has_errors = True
            date_error = 'Date Built is required.'

        if not location:
            has_errors = True
            location_error = 'Location is required.'

        # if not has_errors:
        #     Data_input(db_directory=app_workspace.path, location=location, LowValue1=LowValue1, HighValue1=HighValue1, river=river, date_built=date_built)
        #     return redirect(reverse('lil_people_elcpa:home'))

        messages.error(request, "Please fix errors.")

    # Define form gizmos
    LowValue1 = TextInput(
        display_text='LowValue1',
        name='LowValue1',
        initial=LowValue1,
        error=LowValue1_error,
    )

    HighValue1_input = TextInput(
        display_text='HighValue1',
        name='HighValue1',
        initial=HighValue1,
        error=HighValue1_error
    )

    river_input = TextInput(
        display_text='Weight',
        name='river',
        placeholder='new value',
        initial=river,
        error=river_error
    )

    date_built = TextInput(
        display_text='Low Value 2',
        name='date-built',
        error=date_error
    )

    initial_view = MVView(
        projection='EPSG:4326',
        center=[-98.6, 39.8],
        zoom=3.5
    )

    drawing_options = MVDraw(
        controls=['Modify', 'Delete', 'Move', 'Point'],
        initial='Point',
        output_format='GeoJSON',
        point_color='#FF0000'
    )

    location_input = MapView(
        height='500px',
        width='100%',
        basemap='OpenStreetMap',
        draw=drawing_options,
        view=initial_view,
    )

    add_button = Button(
        display_text='Add',
        name='add-button',
        icon='glyphicon glyphicon-plus',
        style='success',
        attributes={'form': 'Weight-form'},
        submit=True
    )

    cancel_button = Button(
        display_text='Cancel',
        name='cancel-button',
        href=reverse('lil_people_elcpa:home')
    )

    context = {
        'LowValue1': LowValue1,
        'HighValue1_input': HighValue1_input,
        'river_input': river_input,
        'date_built_input': date_built,
        'location_input': location_input,
        'location_error': location_error,
        'add_button': add_button,
        'cancel_button': cancel_button,
    }
    # context = {}

    return render(request, 'lil_people_elcpa/Data_Input.html', context)


@login_required()
def Geoprocessing(request):
    """
    Controller for the Background Page
    """

    context = {}

    return render(request, 'lil_people_elcpa/Geoprocessing.html', context)