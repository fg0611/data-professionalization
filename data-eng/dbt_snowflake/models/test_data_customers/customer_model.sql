-- {{ config(materialized='table') }}

with source_data as (
    select * from {{ source('SNOWFLAKE_SAMPLE_DATA', 'CUSTOMER') }} limit 35
)

select * from source_data
    /*
     Uncomment the line below to remove records with null `id` values
     */
    -- where id is not null