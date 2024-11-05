def post_init_hook(cr, registry):
    """
    This update applies to the city, zip, and state_id fields in the res_partner table. It was necessary because the
    _onchange_city_id method does not trigger upon module installation, leading to incorrect address information by
    retaining outdated values from the l10n_cl_counties module.
    """
    query_to_update_res_partner_info = """
    UPDATE res_partner AS t SET city = c.name, zip = c.zipcode, state_id = c.state_id 
    FROM res_city AS c 
    WHERE t.city_id = c.id AND
    t.city_id IS NOT NULL;
    """
    cr.execute(query_to_update_res_partner_info)
