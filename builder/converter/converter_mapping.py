import list_view
import pipeline_view
import nested_view

converters = {
    'list': list_view.convert_to_xml,
    'pipeline': pipeline_view.convert_to_xml,
    'nested': nested_view.convert_to_xml
}
