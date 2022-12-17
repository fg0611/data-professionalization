-- {{ config(materialized='table') }}

with source_data as (
    select * from {{ source('SNOWFLAKE_SAMPLE_DATA', 'STORE_SALES') }} limit 10
)

select * from source_data
    /*
     Uncomment the line below to remove records with null `id` values
     */
    -- where id is not null