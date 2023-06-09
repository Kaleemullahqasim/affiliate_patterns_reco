import re

# Compile a list of affiliate patterns
patterns = [
    # Existing patterns
    re.compile(r"utm_source=(.+)"),
    re.compile(r"utm_medium=(.+)"),
    re.compile(r"utm_campaign=(.+)"),
    re.compile(r"utm_term=(.+)"),
    re.compile(r"utm_content=(.+)"),
    re.compile(r"ref-id=(.+)"),
    re.compile(r"is_affiliate=(.+)"),
    re.compile(r"affiliate_id=(.+)"),
    re.compile(r"partner_id=(.+)"),
    re.compile(r"tracking_id=(.+)"),
    re.compile(r"aff_id=(.+)"),
    re.compile(r"afftrack=(.+)"),
    re.compile(r"anid=(.+)"),
    re.compile(r"adid=(.+)"),
    re.compile(r"aid=(.+)"),
    re.compile(r"clickid=(.+)"),
    re.compile(r"clickthroughid=(.+)"),
    re.compile(r"commission_id=(.+)"),
    re.compile(r"creative=(.+)"),
    re.compile(r"custom1=(.+)"),
    re.compile(r"custom2=(.+)"),
    re.compile(r"custom3=(.+)"),
    re.compile(r"custom4=(.+)"),
    re.compile(r"custom5=(.+)"),
    re.compile(r"deeplink=(.+)"),
    re.compile(r"destination=(.+)"),
    re.compile(r"offer_id=(.+)"),
    re.compile(r"pid=(.+)"),
    re.compile(r"promo_id=(.+)"),
    re.compile(r"ref=(.+)"),
    re.compile(r"referring_site=(.+)"),
    re.compile(r"source=(.+)"),
    re.compile(r"sub_id=(.+)"),
    re.compile(r"tracking_id=(.+)"),
    re.compile(r"u=(.+)"),
    re.compile(r"utm=(.+)"),
    re.compile(r"visit_id=(.+)"),
    # New patterns
    re.compile(r"tag=(.+)"),  # Amazon
    re.compile(r"linkCode=(.+)"),  # Amazon
    re.compile(r"ref=(.+)"),  # Amazon
    re.compile(r"ascsubtag=(.+)"),  # Amazon
    re.compile(r"associate-tag=(.+)"),  # Amazon
    re.compile(r"banner_id=(.+)"),
    re.compile(r"campaignid=(.+)"),
    re.compile(r"affkey=(.+)"),
    re.compile(r"sid=(.+)"),
    re.compile(r"aff_sub=(.+)"),
    re.compile(r"aff_sub2=(.+)"),
    re.compile(r"aff_sub3=(.+)"),
    re.compile(r"aff_sub4=(.+)"),
    re.compile(r"aff_sub5=(.+)"),
    re.compile(r"source_id=(.+)"),
    re.compile(r"publisher_id=(.+)"),
    re.compile(r"distributor_id=(.+)"),
    re.compile(r"channel_id=(.+)"),
    re.compile(r"affname=(.+)"),
    re.compile(r"affcode=(.+)"),
    re.compile(r"campaign_name=(.+)"),
    re.compile(r"media_id=(.+)"),
    re.compile(r"placement_id=(.+)"),
    re.compile(r"subid1=(.+)"),
    re.compile(r"subid2=(.+)"),
    re.compile(r"subid3=(.+)"),
    re.compile(r"subid4=(.+)"),
    re.compile(r"subid5=(.+)"),
    re.compile(r"redirect_id=(.+)"),
    re.compile(r"referrer_id=(.+)"),
    re.compile(r"pcode=(.+)"),
    re.compile(r"ccode=(.+)"),
    re.compile(r"acode=(.+)"),
    re.compile(r"vcode=(.+)"),
    re.compile(r"discount_code=(.+)"),
    re.compile(r"bonus_code=(.+)"),
    re.compile(r"promo_code=(.+)"),
    re.compile(r"deal_id=(.+)"),
    re.compile(r"gclid=(.+)"),
    re.compile(r"msclkid=(.+)"),
    re.compile(r"fbclid=(.+)"),
    re.compile(r"tduid=(.+)"),
    re.compile(r"mcid=(.+)"),
    re.compile(r"a_aid=(.+)"),
    re.compile(r"a_bid=(.+)"),
    re.compile(r"a_cid=(.+)"),
    re.compile(r"site_id=(.+)"),
    re.compile(r"pub_id=(.+)")
]

def is_affiliate_url(url):
    # Check for edge cases
    if url is None:
        raise ValueError("URL cannot be None")
    if not isinstance(url, str):
        raise ValueError("URL must be a string")

    # Check if the URL matches any of the patterns
    for pattern in patterns:
        if pattern.search(url):
            return True

    return False
  
  
