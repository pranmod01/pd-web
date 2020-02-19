from django.conf.urls import url, include
from . import views

#this is where you add any new pages w/ new urls you want!
urlpatterns = [
	#Pranati
	#url(r'^$', views.[view_name]),
	#add others here; refer to django_notes_caroline.txt for notes as to why
	# Home
	# About Us
	# 	Committee breakdown
	# 	Past/alumni
	# Companies
	# 	Contact info (for company-specific things)
	# 	Sponsorship package (tiers) → instructions
	# 	Companies we’ve worked w/ in the past
	# 	Past events
	# 	What we do
	# Scholars
	# 	PD Packet
	# 	New materials from events
	# 	Events calendar
	# 	Faculty/other collabs w/ committees
	# Forum/Opportunities
	# 	[RELINKS TO FORUM]
	# 		Opportunities
	# 		Updates in recruiting timeline (as told by students)
	# 		Suggestions for CR/feedback
	# 		Live-questions/questions in general
	# Settings
	# 	Sign In
	# 	Profile
	# 	Contact Us

	#02/14/20 - Caroline
	url(r'^$', views.home),
	url(r'^corporate_relations$', views.committees),
	url(r'^alumni$', views.alumni),
	url(r'^companies$', views.companies_home),
	url(r'^companies_contact_us$', views.companies_contact_us),
	url(r'^our_history$', views.companies_history),
	url(r'^past_events$', views.past_events),
	url(r'^about_us$', views.what_we_do),
	url(r'^scholars$', views.scholars_home),
	url(r'^professional_development_resources$', views.pd_resources),
	url(r'^recent_resources$', views.new_resources),
	url(r'^calendar$', views.pd_events_calendar),
	url(r'^community_collabs$', views.collab_socials_events),
	url(r'^scholar_feedback$', views.pd_feedback_ideas),
	url(r'^forum$', views.forum),
	url(r'^scholar_opportunities$', views.opportunities),
	url(r'^recruitment$', views.recruitment),
	url(r'^live_event_tools$', views.live_event_tools_dev),
	url(r'^settings$', views.settings),
	url(r'^sign_in$', views.sign_in),
	url(r'^profile$', views.profile),
	url(r'^contact_us$', views.contact_us),
]