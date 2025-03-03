from horrorRedditImg import make_url_list, get_image_list, make_individual_reel

import pandas as pd

from pprint import pprint



URL_list = ['https://www.reddit.com/r/TwoSentenceHorror/comments/1ikce1b/i_slipped_on_the_ice_in_my_woodland_isolated/', 'https://www.reddit.com/r/TwoSentenceHorror/comments/1ik04qw/your_pet_fish_will_pay_the_price_for_your/', 'https://www.reddit.com/r/TwoSentenceHorror/comments/1ik7pfe/were_perfectly_fine_sharks_can_only_smell_blood/', 'https://www.reddit.com/r/TwoSentenceHorror/comments/1ijsmny/crying_and_terrified_the_soldier_pressed_futilely/', 'https://www.reddit.com/r/TwoSentenceHorror/comments/1ika9tz/my_best_friend_dared_me_to_tell_the_new_girl_to/', 'https://www.reddit.com/r/TwoSentenceHorror/comments/1ik278c/and_after_watching_mushroom_cloud_after_mushroom/', 'https://www.reddit.com/r/TwoSentenceHorror/comments/1ik85eb/the_ai_therapist_told_her_that_trauma_wasnt_real/', 'https://www.reddit.com/r/TwoSentenceHorror/comments/1ijt1pf/i_thought_it_was_sweet_when_my_girlfriend/', 'https://www.reddit.com/r/TwoSentenceHorror/comments/1ik3mlh/i_asked_my_mom_to_give_me_something_to_help_clear/', 'https://www.reddit.com/r/TwoSentenceHorror/comments/1ijn19w/i_guess_i_am_not_a_princess_the_new_mother_mused/', 'https://www.reddit.com/r/TwoSentenceHorror/comments/1ikd7tr/i_was_disappointed_when_the_stainless_steel_knife/', 'https://www.reddit.com/r/TwoSentenceHorror/comments/1ik6ud5/whenever_i_drive_by_a_row_of_houses_i_always/', 'https://www.reddit.com/r/TwoSentenceHorror/comments/1ikedqo/i_hate_blood_so_fucking_much/', 'https://www.reddit.com/r/TwoSentenceHorror/comments/1ijup6f/if_i_may_ask_what_was_his_offense_the_lead/', 'https://www.reddit.com/r/TwoSentenceHorror/comments/1ijsbf9/as_i_left_the_farmers_wife_a_bloodless_spool_on/', 'https://www.reddit.com/r/TwoSentenceHorror/comments/1ik8cug/first_hockey_game_and_my_kid_got_a_puck/', 'https://www.reddit.com/r/TwoSentenceHorror/comments/1ijzum4/at_first_i_thought_it_was_a_trick_of_the_light/', 'https://www.reddit.com/r/TwoSentenceHorror/comments/1ijnfic/you_see_there_is_nothing_to_be_scared_of_said_the/', 'https://www.reddit.com/r/TwoSentenceHorror/comments/1ikd4ed/it_was_really_odd_to_see_an_angler_fish_swimming/', 'https://www.reddit.com/r/TwoSentenceHorror/comments/1ikbd5w/i_carefully_put_in_the_pin_number_to_the_bomb/', 'https://www.reddit.com/r/TwoSentenceHorror/comments/1ik95d7/honey_i_promise_you_there_is_no_bad_man_under/', 'https://www.reddit.com/r/TwoSentenceHorror/comments/1ijhdb1/its_so_brave_of_you_to_be_willing_to_testify/', 'https://www.reddit.com/r/TwoSentenceHorror/comments/1ijdyer/she_rode_me_in_the_dark_her_sweatslicked_skin/', 'https://www.reddit.com/r/TwoSentenceHorror/comments/1ijrpg3/i_always_told_my_daughter_she_was/', 'https://www.reddit.com/r/TwoSentenceHorror/comments/1ijwmqu/the_court_rules_that_humans_and_robots_are_both/']

number = 1

list_tup = make_url_list()


print('list of urls and posts')

URL_list = list_tup[0]

check = get_image_list(URL_list, number)

pprint(list_tup[1])

pprint(check)