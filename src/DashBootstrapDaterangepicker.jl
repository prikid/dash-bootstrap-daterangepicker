
module DashBootstrapDaterangepicker
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.0.1"

include("jl/dashbootstrapdaterangepicker.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "dash_bootstrap_daterangepicker",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "dash_bootstrap_daterangepicker.min.js",
    external_url = "https://unpkg.com/dash_bootstrap_daterangepicker@0.0.1/dash_bootstrap_daterangepicker/dash_bootstrap_daterangepicker.min.js",
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "dash_bootstrap_daterangepicker.min.js.map",
    external_url = "https://unpkg.com/dash_bootstrap_daterangepicker@0.0.1/dash_bootstrap_daterangepicker/dash_bootstrap_daterangepicker.min.js.map",
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
