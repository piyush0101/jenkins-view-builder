from builder.converter import list_view
from builder.converter import pipeline_view
from builder.converter import nested_view
from builder.converter import sectioned_view

converters = {
    'list': list_view.convert_to_xml,
    'pipeline': pipeline_view.convert_to_xml,
    'nested': nested_view.convert_to_xml,
    'sectioned': sectioned_view.convert_to_xml
}
